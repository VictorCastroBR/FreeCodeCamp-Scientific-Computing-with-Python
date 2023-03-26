def arithmetic_arranger(problems, answer=False):
  # Verifica se foram passados no máximo 5 problemas
  if len(problems) > 5:
    return 'Error: Too many problems.'

  sentence = ''
  first_line = []
  second_line = []
  third_line = []
  fourth_line = []

  for item in problems:
    a = item.split(' ')[0]
    b = item.split(' ')[2]
    op = item.split(' ')[1]
    space_a = ''
    space_b = ''
    trace = ''

    # Regras
    # Se atende as operações desejadas
    if op not in '+-':
      return "Error: Operator must be '+' or '-'."
    # Se ambos são números
    if not a.isdigit() or not b.isdigit():
      return 'Error: Numbers must only contain digits.'
    # Se possuem no máximo 4 digitos
    if len(a) > 4 or len(b) > 4:
      return 'Error: Numbers cannot be more than four digits.'

    if len(a) > len(b):
      space_a = ''
      space_b = ' ' * (len(a) - len(b))
    else:
      space_a = ' ' * (len(b) - len(a))
      space_b = ''

    # Frase base
    sentence = f'  {space_a}{a}\n{op} {space_b}{b}\n'.split('\n')
    first_line.append(sentence[0])
    second_line.append(sentence[1])
    res = str(int(a) + int(b) if op == '+' else int(a) - int(b))
    space_res = ''

    if sentence[0] > sentence[1]:
      trace = '-' * (len(sentence[0]))
    else:
      trace = '-' * (len(sentence[1]))

    space_res = ' ' * (len(trace) - len(res))
    third_line.append(trace)
    fourth_line.append(f'{space_res}{res}')

  final_sentence = ''

  if answer:
    final_sentence = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(third_line) + '\n' + '    '.join(fourth_line)
  else:
    final_sentence = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(third_line)
  
  return final_sentence
