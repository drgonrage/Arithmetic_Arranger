def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    line1 = []
    line2 = []
    line3 = []
    solutions = []

    for problem in problems:
        parts = problem.split()
        num1, operator, num2 = parts[0], parts[1], parts[2]

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator == "+":
            solution = str(int(num1) + int(num2))
        else:
            solution = str(int(num1) - int(num2))

        width = max(len(num1), len(num2)) + 2
        line1.append(num1.rjust(width))
        line2.append(operator + num2.rjust(width - 1))
        line3.append("-" * width)
        solutions.append(solution.rjust(width))

    arranged_problems = []

    arranged_problems.append("    ".join(line1))
    arranged_problems.append("    ".join(line2))
    arranged_problems.append("    ".join(line3))

    if show_answers:
        arranged_problems.append("    ".join(solutions))

    return "\n".join(arranged_problems)
