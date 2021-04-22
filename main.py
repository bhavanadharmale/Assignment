import datetime
import calendar

dayList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
def findDay(date):
    born = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
    '%Y-%m-%d'
    return (calendar.day_name[born])

def getOutputDict(d):

    outputDict = dict()

    for key, value in d.items():
        day = findDay(key)
        if day not in outputDict:
            outputDict[day] = value
        else:
            outputDict[day] = outputDict[day] + value

    if len(dayList) != len(outputDict.keys()):
        for key_index in range(0, len(dayList)):
            prev_day_value = 0
            next_day_value = 0
            day = dayList[key_index]
            if dayList[key_index] not in outputDict.keys():
                index = key_index
                while True:
                    if index <= 0:
                        break
                    if dayList[index-1] not in outputDict.keys():
                        index -= 1

                    else:
                        prev_day_value = outputDict[dayList[index - 1]]
                        break

                index = key_index
                while True:
                    if index >= len(dayList)-1:
                        break
                    if dayList[index+1] not in outputDict.keys():
                        index += 1
                    else:
                        next_day_value = outputDict[dayList[index+1]]
                        break

                outputDict[day] = (prev_day_value + next_day_value)//2

    return dict(sorted(outputDict.items(), key=lambda x: dayList.index(x[0])))


print("Test-1 Output")
print("------------------------------------------------------------------------------------------------------")
d = {'2020-01-01':4, '2020-01-02':4, '2020-01-03':6, '2020-01-04':8, '2020-01-05':2, '2020-01-06':-6, '2020-01-07':2, '2020-01-08':-2}
print("Input: {}".format(d))
print("Output: {}".format(getOutputDict(d)))

print("----------------------------------------------------------------------------------------------------")
print("Test-2 Output")
d = {'2020-01-01':6, '2020-01-04':12, '2020-01-05':14, '2020-01-06':2, '2020-01-07':4}
print("Input: {}".format(d))
print("Output: {}".format(getOutputDict(d)))