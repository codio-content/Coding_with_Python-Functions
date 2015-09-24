{Run the code}(./read-simple.sh)

Before we look at a concrete example , let's take a look at some example code. 

This code reads in the data and then inspects each field to see whether there  `|c` occurrs in the string. If it does, then it needs to be replaced with a `,`.

## Explanation
Most of the code is explained in the code comments. However, there are a couple of interesting things worth mentioning.

### while
We are using a while loop rather than a for loop because in this instance it is simpler. 

We need a loop because there could be more than one occurrence of `|c` in the string and we need to keep replacing the `|c` until there are no more left.

```javascript
while ( (pos = cols[j].indexOf('|c') ) != -1 ) {
```

This line is interesting because it is doing 2 things at once

1. It is searching for `|c` and assigning the result to `pos`.
1. Having done that, it evaluates the condition to see if it is not equal to -1.
1. If you do this, you **must** wrap the expression to the left of the `!=` in brackets. Not doing so would give a different result.

Another valid, but longer, way of writing this would have been

```javascript
while ( cols[j].indexOf('|c')  != -1 ) {
  pos = cols[j].indexOf('|c')
  cols[j] = cols[j].substring(0, pos) + ',' + cols[j].substring(pos+2)
}
```

You can see that this involves duplication, which is why we shortened it.

### isNan(string)
You would have used this in a challenge in the File Handling Unit. If `string` is a valid string representation of a number, then it returns `true`.

### parseFloat(string)
This useful function converts a string into a floating point number.

### The output
If you examine the output when you run the code. You will see that it contains `\'` characters. This is just Javascript escaping the `'` character. You would not see this of you output the string to the console.

