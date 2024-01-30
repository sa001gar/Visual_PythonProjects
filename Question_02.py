#Program to read n integers and display them as a histogram
import matplotlib.pyplot as plt #importing packages

def read_input():#taking input
    n = int(input("Enter the number of integers: "))
    data = list(map(int, input("Enter the 'integers' separated by space(Like- 0 1 2 3 4 5 ..etc): ").split()))
    return n, data

def display_histogram(n, data): #setup the display logic
    plt.hist(data, bins=max(data)+1, edgecolor='black', align='left')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()
#creating the final logic
def main():
    n, data = read_input()
    display_histogram(n, data)
main()
ch='Y'
while True:
    ch=input("Do you wanna continue:(y/n)")
    ch=ch.upper
    if ch=='N':
        break
    else:main()