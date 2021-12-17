# Neogex Parsing Standard
##### Much like Regex, Neogex allows for string parsing and validation based on a set of requirements. Unlike Regex, however, Neogex is human readable, utilising a SQL-esque structure to construct validation parameters.
### _
###### For example

`neogex("EMAIL with MIN 10 CHAR")` will require an email with a minimum of 10 characters.
We can expand this into more complex queries.
`neogex("TEXT with MIN 8 CHAR and MAX 20 CHAR and includes[1:] {!@#$}")`
This requires a string of text to be a minimum of 8 characters, and a maximum of 20 characters. It must also include at least 1 of the items found in the set proceeding it.

`Keys` describe what is being validated, and `helpers` string together multiple keys.

| Key   |      Definition  
|----------|:-------------:
| `TEXT` |  Simple string/text
| `EMAIL` |    Will validate @ in email
| `NUM` | Will validate number
| `CHAR` | Used for length validation

| Helper   |      Definition  
|----------|:-------------:
| `and` |  Will validate 2 consecutive conditions are met
| `or` |    Will validate 1 or 2 consecutive conditions are met
| `with` | Validates a key includes a conditional argument. (ie, length)
| `includes[n]` | Validates a key including elements from a set. [n] is the number of elements that need to be included. [1] means only 1, whilst [1:] means 1 or more. [1:3] means only 1, 2 or 3 conditions met
| `{n1, n2, n3, ...}` | Follows the includes helper. Characters in here will be used by includes[n]. For example, includes[1] {!@#} would require at least 1, and no more than 1, of those characters (!, @, #) to be present in the string being validated.