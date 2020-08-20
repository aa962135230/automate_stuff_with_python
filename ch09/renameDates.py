import shutil, os, re

date_pattern = re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$   
    """, re.VERBOSE)

for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)
    if mo == None:
        continue
        
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    euro_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part

    abs_working_dir = os.path.abspath('.')
    amer_filename = os.path.join(abs_working_dir, amer_filename)
    euro_filename = os.path.join(abs_working_dir, euro_filename)

    print("Renaming %s to %s ..." % (amer_filename, euro_filename))
    #shutil.move(amer_filename, euro_filename)
