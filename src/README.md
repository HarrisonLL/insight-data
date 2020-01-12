
To solve the problem, I created four functions to solve.

(1) The first function is round_values. The built in round function does not round values properly, so I decided to wrote the function my own.

(2)The second function is sum_values, which builds a dictionary that has a tuple (border, measure, date) as key. So I am able to aggregate values with the same border, measure and date. The final step of this function involves sort the dictionary by key. 

(3)The third function is the main function moving_avg. The idea is to iterate through the sorted dictionary, which is sorted by time in increasing order. Therefore, I am able to calculate the moving average through each iteration.

(4)The fourth function is final_output. The function sorts rows and appends column names to the list. 
