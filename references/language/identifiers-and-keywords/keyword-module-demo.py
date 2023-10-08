# importing the 'keyword' module
import keyword as kw

# listing all the keywords
print('The', len(kw.kwlist), 'keywords of Python are:')
for item in kw.kwlist: # keyword list
    print(item)

# listing all the soft keywords
print('\nThe', len(kw.softkwlist), 'soft keywords of Python are:')
for item in kw.softkwlist:
    print(item)

# checking for a keyword or a soft keyword
print('\n"\'None\' is a keyword." — ', kw.iskeyword('None')) # True
print('"\'none\' is a keyword." — ', kw.iskeyword('none')) # False
print('"\'match\' is a keyword." — ', kw.issoftkeyword('match')) # False
print('"\'match\' is a soft keyword." — ', kw.issoftkeyword('match')) # True
