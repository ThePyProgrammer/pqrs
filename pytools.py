cnt = -1
def pythonshellreact(ans=False, libs='from math import *', funcs=''):
    exec(libs)
    if len(funcs):
        exec(funcs)
    global cnt
    print('Welcome To Python Shell React!','This is a program we created to aid you in writing Python 3 programs.', 'we hope you\'ll enjoy this!', sep="\n", end="\n")
    ans = ans if ans else bool(ans)
    constlst = []
    while True:
        try:
            ui = input('>>> ')
            if 'constlst.append' in ui:
                cnt += 1
                print('this constant has been added\nIt is uploadable by typing constlst[', cnt, ']', sep='')
                continue
            try:    
                ui = eval(ui)
            except:
                ui = exec(ui)
            else:
                if ui is None:
                    continue
                try:
                    uinow = str(ui)
                except:
                    print(ui)
                    ans, prevans = ui, ans 
                else:
                    if 'constantpingyan.substituteadd' in uinow:
                        uinow, uitype = uinow[30:-6], uinow[-4:-1]
                        if uitype == 'num':
                            uinow = float(uinow) if '.' in uinow else int(uinow)
                        constlst.append(uinow)
                        cnt += 1
                        print('this constant has been pinged\nIt is uploadable by typing constlst[', cnt, ']', sep='')
                    
                    else:
                        print(ui)
                        ans, prevans = ui, ans
        except ZeroDivisionError:
            print('Oh no! You divided a number by zero! You can\'t do that, please note that!')

        except ImportError:
            print('Oh no! It seems this import failed! Nevertheless, do persist!')

        except IndexError:
            print('It seems a list has been indexed with an out-of-range number. Don\'t do that!')

        except NameError:
            print('Hey, that variable is unknown! Please do define variable before using them!')

        except SyntaxError:
            print('It seems there is an error in your syntax. You should try and make it right!')

        except TypeError:
            print('It seems a function has been called with a wrong-type variable! Please correct it!')

        except ValueError:
            print('It seems the value inputted in the function is invalid, not because of type! Correct it!')

        except RuntimeError:
            print('Oops! It seems your code took too long. Maybe you could try shortening it!')

        except FileNotFoundError:
            print('Oh no! This file does not seem to exist! It\'s ok, try again later!')

        except AttributeError:
            print('Your attribute assignment/reference seems to fail! Retry!')

        except FloatingPointError:
            print('Oh no! It seems a floating point operation of yours has failed!')

        except KeyError:
            print('It seems this key was not found in the dictionary!')

        except MemoryError:
            print('Oh no! The operation you ran has run out of memeory!')

        except OverflowError:
            print('Oh no! This arithmetic operation is too large to be represented.')

        except (IndentationError, TabError):
            print('Oh, your indent is incorrect! You should correct it!')

        except UnboundLocalError:
            print('Well, it seems your value is incorrect')

        except AssertionError:
            print('Oh no, there has been an assertion error. It seems your sanity-check is running!')

        except KeyboardInterrupt:
            print("It's sad to see you go, but we wish you a happy journey in Python!")
            break

const_ping = lambda num, typestr: 'constantpingyan.substituteadd('+str(num)+', '+typestr+')'
