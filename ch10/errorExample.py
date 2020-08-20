import traceback
def spam():
    bacon()

def bacon():
    try:
        raise Exception('This is the error message.')
    except:
        error_file = open('errorInfo.txt', 'w')
        error_file.write(traceback.format_exc())
        error_file.close()
        print('The tarceback info was written to errorInfo.txt')
        

spam()