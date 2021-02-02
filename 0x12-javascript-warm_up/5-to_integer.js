#!/usr/bin/node
/* script that prints My number: <first argument
converted in integer> if the first argument can be converted
to an integer.
guillaume@ubuntu:~/0x12$ ./5-to_integer.js
Not a number
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js "89"
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js Holberton
Not a number */

const args = process.argv;
if (parseInt(args[2])) {
  console.log(`My number: ${parseInt(args[2])}`);
} else {
  console.log('Not a number');
}
