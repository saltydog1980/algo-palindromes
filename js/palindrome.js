exports.palindrome = function(word) {
    //checking to see if the word is truly a string and if so taking to lowercace, split to array, filter out anything not alpha character then joining
    //then doing the exact same but reversing the array before joining
    //finally returning the boolean for comparing the two 
    if (typeof(word) === 'string') {
        return word.toLowerCase().split('').filter(element => element.match(/[a-z]/)).join()
        === word.toLowerCase().split('').filter(element => element.match(/[a-z]/)).reverse().join();
    //if word type is number I am taking to string so I can split to array, reverse and then join and then using parse int to take back to an int
    //finally returning the boolean for comparing the two
    } else if (typeof(word) === 'number') {
        return word  === parseInt(word.toString().split('').reverse().join(''));
    }
    
};


// palindrome('racecar') //=== true);
// palindrome('Noon') //=== true);
// palindrome('ciVic') //=== true);
// palindrome('nice') //=== false);
// palindrome(434) //=== true);
//palindrome(123) //=== false);

// console.log("The following should be true if you're trying to do the extra portion of this challenge");
// palindrome("Sore was I ere I saw Eros.") //=== true);
// palindrome("A man, a plan, a canal -- Panama") //=== true);
