"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    res = [round(score) for score in student_scores]
    return res


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    students_result = round_scores(student_scores)
    result = [score for score in students_result if score <= 40]
    return len(result)


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    students_result = round_scores(student_scores)
    result = [score for score in students_result if score >= threshold]
    return result


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    leap = (highest - 40) / 4
    res = [int(41 + leap * index) for index in range(0, 4)]

    # for index in range(0, 4):
    #     vals.append(int(41 + leap * index))
    # return vals
    return res


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    return [f"{(item[0] + 1)}. {(item[1][1])}: {(item[1][0])}"
            for item in enumerate(zip(student_scores, student_names))]


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    res = [item for item in student_info if item[1] == 100]
    return res[0] if len(res) > 0 else []


print(perfect_score(student_info=[
      ["Charles", 90], ["Tony", 80], ["Alex", 99]]))
