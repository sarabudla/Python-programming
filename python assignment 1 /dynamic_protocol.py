"""

File   :  protocol.py
History:  7-Sep-2019, 7-Feb-2021 (updated to use f-strings)

Instruct user how to prepare a 3 ml solution of
10 mM NaCl and 0.5 mM MgCl2, given stock solutions
of 1 M NaCl and 0.1 M MgCl2.
"""


def main():
    """Business logic"""

    final_vol = int(input("Please enter the final volume of the solution (ml)"))

     # NaCl
    nacl_stock = int(input("Please enter the NaCl stock (mM)"))
    nacl_final = int(input("Please enter the NaCl final (mM)"))

     # concatenation, notice how we are calculating something here!
    step1 = f"Add {str(final_vol * (nacl_final / nacl_stock))} ml NaCl\n"

     # MgCl2
    mg_stock = int(input("Please enter the MgCl2 stock (mM)"))
    mg_final = float(input("Please enter the MgCl2 final (mM)"))

    step2 = f"Add {str(final_vol * (mg_final / mg_stock ))} ml MgCl2\n"

     # Water
    step3 = f"Add water to a final volume of {str(final_vol)} ml and mix"

     # Protocol, we can then just print things out b/c they have been formatted earlier
    print(step1 + step2 + step3)


if __name__ == '__main__':
    main()
