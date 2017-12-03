from . import checkstring
from django.shortcuts import render

mapping = {'10': 'Ten', '20': 'Twenty', '30': 'Thirty', '40': 'Fourty', '50': 'Fifty', '60': 'Sixty', '70': 'Seventy',
            '80': 'Eighty', '90': 'Ninety' , '100': 'One Hundred', '00': 'Hundred'}

eleven_to_nineteen = {'11': 'Eleven', '12': 'Twelve', '13': 'Thirtheen', '14': 'Fourteen', '15': 'Fifteen', '16': 'Sixteen',
     '17': 'Seventeen', '18': 'Eighteen', '19': 'Ninteen'}

# Create your views here.


def middlenumbers(number):
    from pprint import pprint
    pprint(number)
    if len(number) == 2:
        digit = number[0] + '0'
        if digit in mapping:
            maps = mapping[digit]
            pprint(maps)
            resul = maps + ' ' + checkstring.check10to90(number[1])
    else:
        digit = number[1] + '0'
        if digit in mapping:
            maps = mapping[digit]
            pprint(maps)
            resul = maps + ' ' + checkstring.check10to90(number[2])
    return resul


def three_digit(number):
    if number[0] == '0' and number[1] == '0' and number[2] == '0':
        result = ' '
    elif number[1] == '0' and number[2] == '0':
        result = checkstring.check10to90(number[0]) + ' ' + 'Hundred'
    elif number[0] == '0' and number[1] == '0' and number[2] != 0:

        result = 'and' + '' + checkstring.check10to90(number[2])
    elif number[1] == '0':
        middle = 'and'
        result = checkstring.check10to90(number[0]) + ' ' + 'Hundred' + ' ' + middle + ' ' + checkstring.check10to90(
            number[2])
    elif number[1] != '0' and number[-2:] in eleven_to_nineteen:
        middle = 'and'
        result = checkstring.check10to90(number[0]) + ' ' + 'Hundred' + ' ' + middle + ' ' + eleven_to_nineteen[number[-2:]]
    elif number[1] != '0':
        middle = 'and'
        result = checkstring.check10to90(number[0]) + ' ' + 'Hundred' + ' ' + middle + ' ' + middlenumbers(number)
    elif number[0] == '0':
        result = 'and' + middlenumbers(number[-2:])
    return result


def convert(request):
    result = ''
    if request.POST:
        numberraw = request.POST.get('number')
        if '0' in numberraw[:1]:
            number = numberraw[1:]
        else:
            number = numberraw
        number_count = len(number)
        actual_number = int(number)

        if number_count == 1:
            if actual_number == 1:
                number = 'One'
                return render(request, 'form.html', {'number': number, 'previous': number})
            if actual_number == 2:
                number = 'Two'
                return render(request, 'form.html', {'number': number, 'previous': number})
            if actual_number == 3:
                number = 'Three'
                return render(request, 'form.html', {'number': number, 'previous': number})
            if actual_number == 4:
                number = 'Four'
                return render(request, 'form.html', {'number': number, 'previous': number})
            if actual_number == 5:
                number = 'Five'
                return render(request, 'form.html', {'number': number, 'previous': number})
            if actual_number == 6:
                number = 'Six'
                return render(request, 'form.html', {'number': number, 'previous': number})
            if actual_number == 7:
                number = 'Seven'
                return render(request, 'form.html', {'number': number, 'previous': number})
            if actual_number == 8:
                number = 'Eight'
                return render(request, 'form.html', {'number': number, 'previous': number})
            if actual_number == 9:
                number = 'Nine'
                return render(request, 'form.html', {'number': number, 'previous': number})

        elif number_count == 2 and number[0] == '1' and number[1] != '0':

            if actual_number == 11:
                number = 'Eleven'
                return render(request, 'form.html', {'number': number, 'previous': number})
            if actual_number == 12:
                number = 'Twelve'
                return render(request, 'form.html', {'number': number, 'previous': number})
            if actual_number == 13:
                number = 'Thirtheen'
                return render(request, 'form.html', {'number': number, 'previous': number})
            if actual_number == 14:
                number = 'Fourteen'
                return render(request, 'form.html', {'number': number, 'previous': number})
            if actual_number == 15:
                number = 'Fifteen'
                return render(request, 'form.html', {'number': number, 'previous': number})
            if actual_number == 16:
                number = 'Sixteen'
                return render(request, 'form.html', {'number': number, 'previous': number})
            if actual_number == 17:
                number = 'Seventeen'
                return render(request, 'form.html', {'number': number, 'previous': number})
            if actual_number == 18:
                number = 'Eighteen'
                return render(request, 'form.html', {'number': number, 'previous': number})
            if actual_number == 19:
                number = 'Ninteen'
                return render(request, 'form.html', {'number': number, 'previous': number})

        elif number_count == 2 and number[1] == '0':
            if number in mapping:
                return render(request, 'form.html', {'number': mapping[number],  'previous': number})

        elif number_count == 2 and number[1] != '0':
            from pprint import pprint
            pprint(number)
            print('line 264')
            digit = number[0] + '0'
            if digit in mapping:
                maps = mapping[digit]
                pprint(maps)
                result = maps + ' ' + checkstring.check10to90(number[1])
            return render(request, 'form.html', {'number': result, 'previous': number})
        # Hundred
        elif number_count == 3:
            if number[1] and number[2] == '0':
                result = checkstring.check10to90(number[0]) + ' ' + 'Hundred'
            elif number[1] == '0':
                middle = 'and'
                result = checkstring.check10to90(number[0]) + ' ' + 'Hundred' + ' ' + middle + ' ' + checkstring.check10to90(number[2])
            elif number[1] != '0':
                middle = 'and'
                result = checkstring.check10to90(number[0]) + ' ' + 'Hundred' + ' ' + middle + ' ' + middlenumbers(number)
            return render(request, 'form.html', {'number': result, 'previous': number})

        #  THOUSAND
        elif number_count == 4:

            if number[1] != '0' and number[2] != '0' and number[3] != '0':
                print('line 92')
                print(number[1:])
                result = checkstring.check10to90(number[0]) + ' ' + 'Thousand' + three_digit(number[1:])

               # case one thousand and one to ten
            elif number[1] == '0' and number[2] == '0' and number[3] != '0':
                print('line 96')
                result = checkstring.check10to90(number[0]) + ' ' + 'Thousand' + ' and' + checkstring.check10to90(number[3])
                # case one thousand and ten to ninety
            elif number[1] == '0' and number[2] != '0' and number[3] != '0':
                print('line 102')
                result = checkstring.check10to90(number[0]) + ' ' + 'Thousand' + ' , ' + middlenumbers(number[-3:])
            elif number[1] == '0' and number[2] != '0' and number[3] == '0':
                print('line 101')
                result = checkstring.check10to90(number[0]) + ' ' + 'Thousand' + ' and' + mapping[number[2:]]

            elif number[1] == '0' and number[2] == '0' and number[3] == '0':
                print('line 105')
                result = checkstring.check10to90(number[0]) + ' ' + 'Thousand'

                # case one thousand and hundred
            elif number[1] != '0' and number[2] == '0' and number[3] == '0':
                print('line 110')
                result = checkstring.check10to90(number[0]) + ' ' + 'Thousand' + ' ' + checkstring.check10to90(number[1]) + 'Hundred'

            elif number[1] != '0' and number[2] == '0' and number[3] != '0':
                print('line 113')
                result = checkstring.check10to90(number[0]) + ' ' + 'Thousand' + ' ' + three_digit(number[1:])

            return render(request, 'form.html', {'previous': number, 'number': result})

        #   Ten Thousand
        elif number_count == 5:
            twenty_one_to_twenty_nine_range = number[:2]
            if number[1] == '0' and number[2] == '0' and number[3] == '0' and number[4] == '0':
                print('line 119')
                digit = number[:2]
                result = mapping[digit] + ' ' + 'Thousand '
            elif number[:2] in eleven_to_nineteen:
                if number[2] == '0' and number[3] == '0' and number[4] == '0':
                    print('line 119')
                    result = eleven_to_nineteen[number[:2]] + ' ' + 'Thousand '
                else:
                    result = eleven_to_nineteen[number[:2]] + ' ' + 'Thousand ' + three_digit(number[-3:])
            elif twenty_one_to_twenty_nine_range[1] != '0':
                print('line 140')
                from pprint import pprint
                digit = twenty_one_to_twenty_nine_range[0] + '0'
                if digit in mapping:
                    maps = mapping[digit]
                    pprint(maps)
                    result = maps + ' ' + checkstring.check10to90(number[1]) + ' ' + 'Thousand ' + three_digit(number[-3:])
            else:
                digit = number[:2]
                result = mapping[digit] + ' ' + 'Thousand ' + three_digit(number[-3:])

            return render(request, 'form.html', {'previous': number, 'number': result})

        #  hundred thousand

        elif number_count == 6:
            result = three_digit(number[:3]) + ' Thousand ' + three_digit(number[3:])
            print('line 159')
            print(result + 'all')
            return render(request, 'form.html', {'previous': number, 'number': result, })

        #  million

        elif number_count >= 7 and (number_count == 7 or number_count <= 7 or number_count <= 9): #or number_count ==9
            first_part = number[:-6]
            second_part = three_digit(number[-6:-3]) + 'Thousand' + ','
            third_part = three_digit(number[-3:])
            if len(first_part) == 1:
                first_part_result = checkstring.check10to90(first_part) + ' ' + 'Million'
            if len(first_part) == 2:
                if first_part in eleven_to_nineteen:
                    first_part_result = eleven_to_nineteen[first_part] + ' ' + 'Million'
                elif first_part in mapping:
                    first_part_result = mapping[first_part] + ' ' + 'Million'
                else:
                    first_part_result = middlenumbers(first_part) + ' ' + 'Million'
            if len(first_part) == 3:
                first_part_result = three_digit(first_part) + ' ' + ' Million'
            result = first_part_result + second_part + third_part
            return render(request, 'form.html', {'previous': number, 'number': result})

        #   BILLION
        elif number_count >= 10 and (number_count == 10 or number_count <= 10 or number_count <= 12):
            first_part = number[:-9]
            second_part = three_digit(number[-9:-6]) + ' ' + 'Million' + ','
            third_part = three_digit(number[-6:-3]) + 'Thousand' + ','
            fourth_part = three_digit(number[-3:])

            if len(first_part) == 1:
                first_part_result = checkstring.check10to90(first_part) + ' ' + 'Billion'
            if len(first_part) == 2:
                if first_part in eleven_to_nineteen:
                    first_part_result = eleven_to_nineteen[first_part] + ' ' + 'Billion'
                elif first_part in mapping:
                    first_part_result = mapping[first_part] + ' ' + 'Billion'
                else:
                    first_part_result = middlenumbers(first_part) + ' ' + 'Billion'
            if len(first_part) == 3:
                first_part_result = three_digit(first_part) + ' ' + ' Billion'
            result = first_part_result + second_part + third_part + fourth_part
            return render(request, 'form.html', {'previous': number, 'number': result})

        #   Quadrillion
        elif number_count >= 13 and (number_count == 13 or number_count <= 13 or number_count <= 15):
            first_part = number[:-12]
            second_part = three_digit(number[-12:-9]) + 'Billion' + ','
            third_part = three_digit(number[-9:-6]) + 'Million' + ','
            fourth_part = three_digit(number[-6:-3]) + 'Thousand' + ','
            fifth_part = three_digit(number[-3:])
            if len(first_part) == 1:
                first_part_result = checkstring.check10to90(first_part) + ' ' + 'Trillion'
            if len(first_part) == 2:
                if first_part in eleven_to_nineteen:
                    first_part_result = eleven_to_nineteen[first_part] + ' ' + 'Trillion'
                elif first_part in mapping:
                    first_part_result = mapping[first_part] + ' ' + 'Trillion'
                else:
                    first_part_result = middlenumbers(first_part) + ' ' + 'Trillion'
            if len(first_part) == 3:
                first_part_result = three_digit(first_part) + ' ' + 'Trillion'
            result = first_part_result + second_part + third_part + fourth_part + fifth_part
            return render(request, 'form.html', {'previous': number, 'number': result})
#   Quadrillion
        elif number_count >= 16 and (number_count == 16 or number_count <= 16 or number_count <= 18):
            first_part = number[:-15]
            second_part = three_digit(number[-15:-12]) + 'Trillion' + ','
            third_part = three_digit(number[-12:-9]) + 'Billion' + ','
            fourth_part = three_digit(number[-9:-6]) + 'Million' + ','
            fifth_part = three_digit(number[-6:-3]) + 'Thousand' + ','
            sixth_part = three_digit(number[-3:])
            if len(first_part) == 1:
                first_part_result = checkstring.check10to90(first_part) + ' ' + 'Quadrillion'
            if len(first_part) == 2:
                if first_part in eleven_to_nineteen:
                    first_part_result = eleven_to_nineteen[first_part] + ' ' + 'Quadrillion'
                elif first_part in mapping:
                    first_part_result = mapping[first_part] + ' ' + 'Quadrillion'
                else:
                    first_part_result = middlenumbers(first_part) + ' ' + 'Quadrillion'
            if len(first_part) == 3:
                first_part_result = three_digit(first_part) + ' ' + 'Quadrillion'
            result = first_part_result + second_part + third_part + fourth_part + fifth_part + sixth_part
            return render(request, 'form.html', {'previous': number, 'number': result})

        elif number_count >= 18:
            result = number + '  Is So Out Of Earth, If You Ever See Such Ammount please let EFCC Know'
            return render(request, 'form.html', {'previous': number, 'number': result})
    else:
        return render(request, 'Form.html')

