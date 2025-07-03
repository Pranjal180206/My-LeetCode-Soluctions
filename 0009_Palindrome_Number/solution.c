bool isPalindrome(int x) {
    int num = x;
    long reversed_num = 0;
    int last_digit = 0;
    while (num > 0){
        last_digit = num % 10;
        num = num / 10;
        reversed_num = last_digit + reversed_num*10;
    }
    if (x == reversed_num)
        return 1;
    else
        return 0;
}
