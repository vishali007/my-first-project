'''
 Shakuntala’s Challenge

 Method is to split each number x and y into two parts:
 x = 10^(n/2) * a + b,
 y = 10^(n/2) * c + d
 Then, x * y = 10^n(a*c) +10^n/2 (a*d + b*c) + b*d   --> equation (1)

 The design strategy used is Recursive Multiplication Algorithm (Divide & Conquer style)

 In the above equation, x and y have n digits and a, b, c and d have n/2 digits each.
 There are four multiplications (ac, ad, bc, bd) of numbers having size n/2
 (having number of digits equal to n/2). So basically, we divided our multiplication
 problem of size n into four sub-multiplications of size n/2.

 But still the time complexity of the recurrence relation formed
              T(n)=4T(n/2)+O(n) is O(n^2)

 Here, the first term accounts for the four multiplication of size n/2 and the second
 term is accounts for addition operation in the given equation (1)

 Using Master Theorem, T(n)=aT(n/b)+O(n^d)
 where a ≥ 1, b≥1, d≥ 0
 There are 3 cases for the master theorem:
 Case 1: d < log(a) [base b] => Time Complexity = O(n ^ log(a) [base b])
 Case 2: d = log(a) [base b] => Time Complexity = O((n ^ d) * log(n) )
 Case 3: d > log(a) [base b] => Time Complexity = O((n ^ d))

 For the above case: a = 4, b = 2 and d = 1
 log(a) [base b] => log(4) [base 2] => 2

 This falls under Case 1: d < log(a) [base b]  => 1 < 2
 Time Complexity = O(n ^ log(a) [base b]) => O(n^2)

 We need to reduce the time complexity. Therefore, the trick is to split
 the middle part of the above equation (1) as shown below,
              (ad+bc)=(a+b)(c+d)−ac−bd

 As the multiplications ac and bd are already calculated in the equation (1), we reduced
 the multiplications ad and bc into one multiplication (a+b)∗(c+d)

 The resultant equation becomes as shown below,
                X∗Y= 10^(n)∗(ac)+ 10^(n/2)∗((a+b)∗(c+d)−ac−bd)+bd

 Therefore, there are now three multiplications of size n/2 (having number of digits equal to n/2)
 and the recurrence relation formed is
                T(n)=3T(n/2)+O(n)

 Here, the first term accounts for the three multiplication of size n/2 and the second
 term is accounts for addition & subtraction operation in the given equation (1)

 Using Master Theorem, T(n)=aT(n/b)+O(n^d)
 where a ≥ 1, b≥1, d≥ 0
 There are 3 cases for the master theorem:
 Case 1: d < log(a) [base b] => Time Complexity = O(n ^ log(a) [base b])
 Case 2: d = log(a) [base b] => Time Complexity = O((n ^ d) * log(n) )
 Case 3: d > log(a) [base b] => Time Complexity = O((n ^ d))

 For the above case: a = 3, b = 2 and d = 1
 log(a) [base b] => log(3) [base 2] => 1.58496

 This falls under Case 1: d < log(a) [base b]  => 1 < 1.58496
 Time Complexity = O(n ^ log(a) [base b]) => O(n^1.58496)

 The resultant equation becomes as shown below,
                X∗Y= 10^2*floor(n/2)∗(ac)+ 10^floor(n/2)∗((a+b)∗(c+d)−ac−bd)+bd
'''
#--------------------------------------------------------------------------
#  Import Statements
#--------------------------------------------------------------------------
import sys, re, os

# Checking Python Version before running the script
if sys.version_info[0] < 3:
    # Exit for Python 2
    print ("The script is written in Python 3.7 and cannot be \
        executed in a python 2 version")
    sys.exit()
elif sys.version_info[0] == 3 & sys.version_info[1] > 7:
    print ("The script is written in Python 3.7 and executing this \
        in a version greater than 3.7 might not work as expected. \
        So giving you a prior headsup****")
else:
    pass

# changing the directory to the location where this script is present
# expecting inputPS13.txt and outputPS13.txt to be available in this location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
#--------------------------------------------------------------------------
#  Definition of the multiplication function
#--------------------------------------------------------------------------
def multiplication(X, Y, outfile):
    # if the given number is a single digit then directly multiply it
    if abs(X) < 10 or abs(Y) < 10:
        return X * Y
    else:
        outfile.write("-" * 50 + "\n")
        outfile.write(f"1st number, x: {X} \n")
        outfile.write(f"2nd number, y: {Y} \n")
        outfile.write(f"Intermediate Values of A,B after partition: \n")
        # Determine the maximum size (number of digits) of the input numbers which is
        # achieved by converting the numbers into strings and calculating the length of the strings

        n = max(len(str(X)), len(str(Y)))
        # Determine size n/2 (having number of digits equal to n/2)
        # // is used to be interpreted as floor division
        # This floor division ensures that exponents remain entire numbers
        split_ptr = n//2
        # Divide X into (a and b) and Y into (c and d) such that their former parts
        # (a and c) always get the extra digit in case the size (n) is odd
        split = 10 ** (split_ptr)
        a = X // split
        b = X % split
        c = Y // split
        d = Y % split
        outfile.write(f"x: {X} a : {a} b : {b} \n")
        outfile.write(f"y: {Y} c : {c} d : {d} \n")
        # 3 calls made to numbers approximately half the size
        z2 = multiplication(a, c, outfile)
        if len(str(a)) >= 2 or len(str(c)) >=2 :
            outfile.write(f"Intermediate Product: {a} x {c} = {z2} \n")
            outfile.write("-" * 50 + "\n")

        z0 = multiplication(b, d, outfile)
        if len(str(b)) >= 2 or len(str(d)) >=2 :
            outfile.write(f"Intermediate Product: {b} x {d} = {z0} \n")
            outfile.write("-" * 50 + "\n")

        z1 = multiplication((a + b), (c + d), outfile)
        if len(str(a)) >= 2 or len(str(c)) >=2 :
            outfile.write(f"Intermediate Product: {a+b} x {c+d} = {z1} \n")
            outfile.write("-" * 50 + "\n")

        # return the resultant equation
        return (z2 * 10**(2*split_ptr)) + ((z1 - z2 - z0) * 10**(split_ptr)) + (z0)
    # End of multiplication function
#--------------------------------------------------------------------------
#  __main__
#--------------------------------------------------------------------------
if __name__ == '__main__':
    #--------------------------------------------------------------------------
    #  Reading the Input from inputPS13 text file
    #--------------------------------------------------------------------------
    try:
        with open("inputPS13.txt", "r") as f:
            num = []
            for index, eachline in enumerate(f.readlines()):
                    # Expected Input pattern:
                    # Number 1: *****
                    # Number 2: *****
                    if all([term.lower() in eachline.lower() for term in ["Number"]]):
                        eachline = re.sub(r",", "", eachline)
                        m = re.search(r"Number\s*(\d+)\s*[:=]?\s*(\d+)", eachline, re.IGNORECASE)
                        if m:
                            num.append(m.group(2).rstrip())
                        else:
                            print(f"No number found in Line no {index + 1}: \"{eachline.rstrip()}\"")
                    else:
                        print(f"No number found in Line no {index + 1}: \"{eachline.rstrip()}\"")
    except Exception as e:
        print(f"Exception: {e}")
    # Retrieving the value of X and Y
    if(len(num)==2):
        X = int(num[0])
        Y = int(num[1])
        # --------------------------------------------------------------------------
        #  Writing to the Output file - outputPS13 text file
        # --------------------------------------------------------------------------
        with open("outputPS13.txt", "w") as outfile:
            # calling the multiplication method
            res = multiplication(X, Y, outfile)
            outfile.write(f"Intermediate Product: {X} x {Y} = {res} \n")
            outfile.write("-" * 50 + "\n")
            outfile.write(f"Result:> {X} x {Y} = {res} \n")
    else:
        print(f"No sufficient input provided")
# --------------------------------------------------------------------------
#  END OF SCRIPT
# --------------------------------------------------------------------------
