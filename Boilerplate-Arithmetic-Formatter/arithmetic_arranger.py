def arithmetic_arranger(problems, results = False):

  import re

  if len(problems) > 5:
    arranged_problems = "Error: Too many problems."
    return arranged_problems

  arranged_problems = 0
  bigrow_0 = 0
  bigrow_1 = 0
  bigrow_lines = 0
  bigrow_2 = 0

  for element in problems:
    num_0 = re.match(r"(\S*)\s", element).group(1)
    num_1 = re.match(r".+\s(\S*)$", element).group(1)
    sym_0 = re.match(r".+\s(\W)\s", element).group(1)

    if sym_0 not in {"+", "-"}:
      arranged_problems = "Error: Operator must be '+' or '-'."
      return arranged_problems

    if num_0.isdigit() == False or num_1.isdigit() == False:      
      arranged_problems = "Error: Numbers must only contain digits."
      return arranged_problems 

    if len(num_0) > 4 or len(num_1) > 4:
      arranged_problems = "Error: Numbers cannot be more than four digits."
      return arranged_problems  

    if sym_0 == "+":
      res = int(num_0) + int(num_1)
    else: 
      res = int(num_0) - int(num_1)
    
    width = max(len(num_0), len(num_1)) + 2
    sp_0 = width - len(num_0)
    row_0 = sp_0*" " + str(num_0)
    sp_1 = width - len(num_1) - 1
    row_1 = str(sym_0) + sp_1*" " + str(num_1)
    lines = width*"-"
    sp_2 = width - len(str(res))
    row_2 = sp_2*" " + str(res) 

    if bigrow_0 == 0:
      bigrow_0 = row_0
      bigrow_1 = row_1
      bigrow_lines = lines
      bigrow_2 = row_2
    else:
      bigrow_0 += 4*" " + row_0
      bigrow_1 += 4*" " + row_1
      bigrow_lines += 4*" " + lines
      bigrow_2 += 4*" " + row_2

  if results == True:
    arranged_problems = "{}\n{}\n{}\n{}".format(bigrow_0, bigrow_1,
                                              bigrow_lines, bigrow_2)
  else:
    arranged_problems = "{}\n{}\n{}".format(bigrow_0, bigrow_1,
                                              bigrow_lines)

  return arranged_problems
