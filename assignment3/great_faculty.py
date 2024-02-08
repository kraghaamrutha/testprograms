from collections import defaultdict
from assignment3.common import students_data, sub_fac_data


max_marks = defaultdict(list)
for roll_no, data in students_data.items():
    for sub_id, marks in data['marks'].items():
        if marks > 90:
            max_marks[sub_id].append(roll_no)
sid, roll_nums = max(max_marks.items(), key = lambda x: len(x[1]))

print(sub_fac_data[sid]['faculty_name'], sub_fac_data[sid]['name'], len(roll_nums))



# ---------IN FUNCTIONS---------

# def great_faculty():
#     """
#     return:dict
#     """
#     max_marks = defaultdict(list)
#     for roll_no, data in students_data.items():
#         for sub_id, marks in data['marks'].items():
#             if marks > 90:
#                 max_marks[sub_id].append(roll_no)
#     sid, roll_nums = max(max_marks.items(), key = lambda x: len(x[1]))
    
    
#     return{
#         "faculty_name":sub_fac_data[sid]['faculty_name'],
#         "name":sub_fac_data[sid]['name'],
#         "roll_nums":len(roll_nums),
#     }


# if __name__ == '__main__':
#     print(great_faculty())
