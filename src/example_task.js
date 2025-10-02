// Example Task - Palindrome Checker

function isPalindrome(str) {
    """
    Check if a given string is a palindrome.
    A clean code implementation should be simple and easy to understand.
    """
    const cleanedStr = str.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    const reversedStr = cleanedStr.split('').reverse().join('');
    return cleanedStr === reversedStr;
}

console.log(isPalindrome("A man, a plan, a canal: Panama")); // true
console.log(isPalindrome("hello")); // false
