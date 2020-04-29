# a function to check if a string of text is a US phone number (xxx-xxx-xxxx)
def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal:
            return False
    return True

print('Is 415-555-4242 a phone number?')
print(is_phone_number('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(is_phone_number('Moshi moshi'))
print('Is 000-000-0000 a phone number?')
print(is_phone_number('000-000-0000'))
print('Is 000-0O0-0000 a phone number?')
print(is_phone_number('000-0O0-0000'))

# to find a phone number in a long chunk of text
def phone_number_finder(text):
    for i in range(len(text)):
        chunk = text[i:i+12]
        if is_phone_number(chunk):
            print(f"Found phone number; {chunk}")

phone_number_finder('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')
phone_number_finder("906-458-2061  Cell Number, from Marquette, MI(state),USA  516-465-9605  Landline, from Hicksville, NY(state),USA  516-977-5990  Landline, from Farmingdale, NY(state),USA  850-451-0892  Cell Number, from Altha, FL(state),USA  925-225-0006  Cell Number, from Pleasanton, CA(state),USA  305-741-9384  Landline, from Marathon, FL(state),USA  985-277-5703  Landline, from Hammond, LA(state),USA  606-408-2444  Landline, from Ashland, KY(state),USA  606-282-9136  Landline, from Stanford, KY(state),USA  978-473-9744  Cell Number, from Beverly, MA(state),USA  570-285-5735  Landline, from Kingston, PA(state),USA  414-588-0708  Cell Number, from Milwaukee, WI(state),USA  304-455-0402  Landline, from New Martinsville, WV(state),USA  860-668-7487  Landline, from Windsor Locks, CT(state),USA  817-744-2885  Landline, from Keller, TX(state),USA  561-758-4575  Cell Number, from Palm Beach, FL(state),USA  845-438-9372  Cell Number, from Newburgh, NY(state),USA  815-804-0157  Landline, from Pecatonica, IL(state),USA  601-444-1393  Landline, from Columbia, MS(state),USA  205-912-4838  Landline, from Birmingham, AL(state),USA  718-661-1491  Landline, from Flushing, NY(state),USA  347-626-6389  Landline, from Saint Albans, NY(state),USA  323-399-8492  Cell Number, from Montebello, CA(state),USA  469-734-9112  Cell Number, from Mckinney, TX(state),USA  231-829-1078  Landline, from Tustin, MI(state),USA  508-849-3854  Landline, from Worcester, MA(state),USA  740-437-6156  Landline, from Bloomingburg, OH(state),USA  407-428-5052  Landline, from Orlando, FL(state),USA  425-221-2939  Cell Number, from Bellevue, WA(state),USA  812-955-6668  Landline, from Bloomington, IN(state),USA  919-356-1286  Cell Number, from Sanford, NC(state),USA  408-868-7168  Landline, from Saratoga, CA(state),USA  717-398-2648  Cell Number, from Gettysburg, PA(state),USA  515-328-0393  Landline, from Story City, IA(state),USA  229-449-9769  Cell Number, from Albany, GA(state),USA  312-516-0585  Landline, from Chicago, IL(state),USA  714-678-8757  Landline, from Anaheim, CA(state),USA  727-896-0740  Landline, from Saint Petersburg, FL(state),USA  570-517-2607  Landline, from Stroudsburg, PA(state),USA  360-665-1363  Landline, from Ocean Park, WA(state),USA  872-225-4779  Landline, from Chicago, IL(state),USA  701-255-5740  Landline, from Bismarck, ND(state),USA  507-361-5661  Landline, from Winona, MN(state),USA  262-399-7391  Cell Number, from Racine, WI(state),USA  540-836-8007  Cell Number, from Staunton, VA(state),USA  832-459-3681  Cell Number, from Houston, TX(state),USA  814-312-0412  Landline, from Altoona, PA(state),USA  575-952-3795  Cell Number, from Truth Or Consequences, NM(state),USA  973-648-6639  Landline, from Newark, NJ(state),USA  614-448-2867  Landline, from Columbus, OH(state),USA  714-656-6502  Landline, from Santa Ana, CA(state),USA  716-236-5781  Landline, from Niagara Falls, NY(state),USA  419-928-0795  Landline, from Polk, OH(state),USA  714-442-1782  Landline, from Santa Ana, CA(state),USA  360-690-0034  Landline, from Vancouver, WA(state),USA  419-486-0188  Landline, from Toledo, OH(state),USA  847-498-4001  Landline, from Northbrook, IL(state),USA  320-353-0806  Landline, from Richmond, MN(state),USA  619-732-0106  Landline, from San Diego, CA(state),USA  240-435-6786  Cell Number, from Waldorf, MD(state),USA  843-289-9839  Cell Number, from Marion, SC(state),USA  847-856-2874  Landline, from Gurnee, IL(state),USA  760-684-5398  Landline, from Victorville, CA(state),USA  201-541-8597  Landline, from Englewood, NJ(state),USA  917-209-1328  Cell Number, from New York, NY(state),USA  631-367-5277  Landline, from Cold Spring Harbor, NY(state),USA  214-248-4090  Cell Number, from Grand Prairie, TX(state),USA  646-872-2891  Cell Number, from New York, NY(state),USA  765-439-5549  Cell Number, from Centerville, IN(state),USA  832-401-4565  Cell Number, from Cleveland, TX(state),USA  952-657-3004  Landline, from Mayer, MN(state),USA  502-514-5933  Landline, from Owenton, KY(state),USA  919-638-5260  Cell Number, from Durham, NC(state),USA  619-709-9437  Cell Number, from San Diego, CA(state),USA  920-425-9973  Landline, from De Pere, WI(state),USA  206-777-8034  Landline, from Seattle, WA(state),USA  425-391-6711  Landline, from Issaquah, WA(state),USA  626-307-0840  Landline, from Alhambra, CA(state),USA  812-201-8670  Cell Number, from Terre Haute, IN(state),USA  330-926-1445  Landline, from Akron, OH(state),USA  814-694-2245  Landline, from Spartansburg, PA(state),USA  404-279-4189  Landline, from Atlanta, GA(state),USA  949-596-3658  Cell Number, from Irvine, CA(state),USA  985-486-8776  Landline, from Hammond, LA(state),USA  254-235-4620  Landline, from Waco, TX(state),USA  618-837-0304  Cell Number, from Olney, IL(state),USA  505-798-4102  Landline, from Albuquerque, NM(state),USA  402-853-9809  Landline, from Lincoln, NE(state),USA  313-549-3117  Cell Number, from Detroit, MI(state),USA  267-544-1736  Landline, from Mechanicsville, PA(state),USA  215-496-1910  Landline, from Philadelphia, PA(state),USA  917-974-0118  Cell Number, from Brooklyn, NY(state),USA  520-405-0556  Cell Number, from Tucson, AZ(state),USA  501-813-0928  Landline, from Little Rock, AR(state),USA  617-691-7165  Landline, from Quincy, MA(state),USA  661-206-1541  Landline, from Lancaster, CA(state),USA  415-564-8492  Landline, from San Francisco, CA(state),USA  814-843-6080  Cell Number, from Altoona, PA(state),USA  203-808-5646  Cell Number, from Waterbury, CT(state),USA  770-286-4799  Landline, from Atlanta, GA(state),USA  608-767-2571  Landline, from Black Earth, WI(state),USA  509-680-4360  Cell Number, from Colville, WA(state),USA  562-277-3658  Landline, from Long Beach, CA(state),USA  215-667-1432  Landline, from Philadelphia, PA(state),USA  936-396-1089  Landline, from Normangee, TX(state),USA  620-644-5337  Landline, from Fort Scott, KS(state),USA  910-804-2527  Landline, from Fayetteville, NC(state),USA  860-224-9814  Landline, from New Britain, CT(state),USA  626-535-2732  Landline, from Pasadena, CA(state),USA  319-754-9709  Landline, from Burlington, IA(state),USA  505-273-2325  Cell Number, from Albuquerque, NM(state),USA  385-375-6773  Cell Number, from Provo, UT(state),USA  301-433-5509  Landline, from Fort Washington, MD(state),USA  925-570-6545  Cell Number, from San Ramon, CA(state),USA  402-365-8597  Landline, from Deshler, NE(state),USA  603-426-8890  Cell Number, from Derry, NH(state),USA  719-251-1594  Cell Number, from Pueblo, CO(state),USA  858-905-5678  Landline, from San Diego, CA(state),USA  347-802-3249  Landline, from New York, NY(state),USA  718-804-3522  Landline, from Brooklyn, NY(state),USA")