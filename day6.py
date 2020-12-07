from utils import get_lines_from_file


if __name__ == '__main__':
    lines = get_lines_from_file('inputs/day6.txt', sep='\n\n')
    total = 0

    # Part 1
    for group in lines:
        unique_question_answers = set([char for char in group if char != "\n"])
        total += len(unique_question_answers)
    print(f"Found a total of {total} unique answers for all groups")

    # Part 2, let's use sets and do their intersection for each group
    # then we simply do the sum of the length of all the intersections
    intersection_total = 0
    for group in lines:
        one_person_answers = [elt for elt in group.split('\n') if elt]
        intersection_for_group = set(one_person_answers[0])
        for one_answer in one_person_answers:
            intersection_for_group = intersection_for_group.intersection(set(one_answer))
        intersection_total += len(intersection_for_group)

    print(f"Found an intersection total of {intersection_total} common answers")
