# let's make them fancier
# we can use and / or to allow for more complicated statemetns

# and will evalute True if both statements are True

i = 6
if i < 10 and i > 5:
    print('true')

if i < 5 or i < 10:
    print("this is a true statment")

if (i > 5 and i < 10) or i > 100:
    print("i fits the criteria")

# in and not statements are also very true
if "run" in "I run the team":
    print(True)
 
if "yum" not in "I run the team":
    print('not found')

pod = False

if not pod:
    print('pod')