# pyquoter
A CLI tool to save your favorite quotes :).

## Installation
```
pip install pyquoter
```

## Usage 
All of the flags and options are visible with the `--help` flag

### Creating quotes
```bash
pyquoter -q "This is the quote!" -a "Author Name!" -d 11/20/2020 -t These are Tags

pyquoter -q "This Another quote" -d 11/20/2020 -t cool inspirational # Author defaults to Unkown

pyquoter -q "Just testing stuff" # All that is required is the quote
```

### Searching quotes
To turn a quote insertion into a query just add the -f flag
```bash
pyquoter -f -q "quote" # Outputs quotes that contain the word "quote"

pyquoter -f -a "Abraham" # Outputs quotes with any author the word "Abraham" in their name

pyquoter -f -i 1 # Outputs the quote with an ID of 1

pyquoter -f -t inspirational # Outputs any quote tagged with the world inspirational

pyquoter -f # Outputs all the quotes
```

Sample output:
```
[3] Pyquoter is alright I guess
 - Josh 11/20/2020
```

### Deleting quotes
If you have a quote that you think isn't up to par, you can delete it by referencing its ID
```bash
pyquoter --delete 1 # Deletes the quote with an ID of 1
```


## Creating an Alias
Typing pyquoter may be a bit verbose so if you have a .bashrc add the line
```alias pq=pyquoter``` 


