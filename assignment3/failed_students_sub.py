from collections import defaultdict
from assignment3.common import students_data, sub_fac_data

#  ---------failed students-------

# sub_failed = defaultdict(list)
# for roll_no, data in students_data.items():
#     for sub_id, marks in data['marks'].items():
#         if marks < 35:
#             sub_failed[sub_id].append(roll_no)

# print(sub_failed)



# --------IN FUNCTIONS--------

# def failed_student():
#     """
#     :return:dict
#     """
#     sub_failed = defaultdict(list)
#     for roll_no, data in students_data.items():
#         for sub_id, marks in data['marks'].items():
#             if marks < 35:
#              sub_failed[sub_id].append(roll_no)
         
#     return {
#        "sub_failed":sub_failed,
#     }

        
# if __name__ == '__main__':
#     print(failed_student())




# print("-------------------")
# # for sub_id, roll_nums in sub_failed.items():
# #     print(f"{sub_fac_data[sub_id]['name']} ({len(roll_nums)})")
# #     print("-------------------")
# #     for roll_no in roll_nums:
# #         print(students_data[roll_no]['name'])
# #     print("-------------------")




#----------- Subject wise toppers------------


# sub_failed = defaultdict(list)
# for roll_no, data in students_data.items():
#     for sub_id, marks in data['marks'].items():
#         if marks == 100:
#             sub_failed[sub_id].append(roll_no)

# print("-------------------")
# for sub_id, roll_nums in sub_failed.items():
#     print(f"{sub_fac_data[sub_id]['name']} ({len(roll_nums)})")
#     print("-------------------")
#     for roll_no in roll_nums:
#         print(students_data[roll_no]['name'])
#     print("-------------------")


# # -----------IN FUNCTION----------

def failed_student():
    """
    :return:dict
    """
    sub_failed = defaultdict(list)
    for roll_no, data in students_data.items():
        for sub_id, marks in data['marks'].items():
            if marks == 100:
                sub_failed[sub_id].append(roll_no)

    print("-------------------")
    for sub_id, roll_nums in sub_failed.items():
        print(f"{sub_fac_data[sub_id]['name']} ({len(roll_nums)})")
        print("-------------------")
        for roll_no in roll_nums:
            print(students_data[roll_no]['name'])
        print("-------------------")

    return{
        "faculty_name":sub_fac_data[sub_id]['faculty_name'],
        "name":sub_fac_data[sub_id]['name'],
        "roll_no":len(roll_no),
    }
    
    
    
if __name__ == '__main__':
    print(failed_student())
