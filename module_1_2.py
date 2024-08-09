qnty_of_tasks = 12
qnty_of_hours = 1.5
name_of_course = 'Python'
time_per_one_task = qnty_of_hours/qnty_of_tasks
#option1
print('Курс :',name_of_course,', всего задач:',qnty_of_tasks,', затрачено часов:',qnty_of_hours,', среднее время выполнения :',time_per_one_task,' часа.')

#option2
time_per_one_task = str(qnty_of_hours/qnty_of_tasks)
final_string ='Курс : '+name_of_course+', всего задач: '+str(qnty_of_tasks)+', затрачено часов: '+str(qnty_of_hours)+', среднее время выполнения : '+time_per_one_task+' часа.'
print(final_string)

