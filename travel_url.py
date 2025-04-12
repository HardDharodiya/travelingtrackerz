
        
def get_bus_route(bus_number, sData, dData):
    try:
        if bus_number < 0 or bus_number >= len(sData):
            raise ValueError
        SOURCE = "+".join(sData[bus_number].split())
        DESTINATION = "+".join(dData[bus_number].split())
        URL = f"https://www.google.com/maps/dir/{SOURCE}+bus+stop,+Rajkot,+Gujarat/${DESTINATION}+bus+stop,+Rajkot,+Gujarat/"
        return SOURCE, DESTINATION, URL
    except ValueError:
        return None, None, "Invalid bus number. Please try again."

def main():
    sData=["-", "Saurashtra University", "Pradyuman Park", "Jivraj Park", "Aajidam ", "Raiya Gaam", "Santoshinagar", "Bajrangvadi Circle", "Greenland Chokadi", "Arpit Eng. College (Hadala Gam)", "-", "Shapar Veraval", "-", "Kothariya Chokadi", "Kothariya Gam", "G.I.D.C. Gate 3", "Kothariyagam", "Saurashtrar University", "Aajidam ", "131 Slam Quarter", "Ghanteshvar S.R.P. Camp", "Marketing Yard", "-", "Mavdi Gam", "G.I.D.C. Gate 3", "131 Slam Quarter", "Santoshinagar", "Raiyadhar Salam Quarter", "Gujarat Housing Quarter", "-", "Trikon Baug circular", "-", "Parsananagar", "Ashapura Mandir", "Marketing Yard", "Shapar Veraval", "Bhakatinagar Circle", "Chhatrapati Shivaji Township", "Aajidam ", "-", "Santoshinagar", "Gangotri Park", "Greenland Chokadi", "Akshar Vatika", "Tramba Gam", "Ratanpar", "Arpit Eng. College (Hadala Gam)", "Kothariyagam", "-", "-", "-", "Punit Nagar", "-", "-", "Kothariya Chokadi", "Gondal Chokadi", "-", "Government Eng. College"]
    dData=["-", "Trikon Baug", "Raiya Gaam", "Madhapar Chokadi", "G.I.D.C. Gate 3", "Tramba", "Tramba Gam", "Bhakatinagar Circle", "Labhubhai Engineering College", "Saurashtra University", "-", "Trikon Baug", "-", "Lal bahadur shastriavas", "Navagam", "Kothariya Gam", "Saurashtra University", "Tramba Gam", "G.I.D.C. Gate 3", "Vavdi Gam", "Shapar Veraval", "Shantiniketan aveue (Raiya Gam)", "-", "Pradyuman Park", "Trikon Baug", "Jivraj Park", "Vavdi Gam", "Trikon Baug", "Jivraj Park", "-", "Trikon Baug", "-", "Tramba Gam", "Parsananagar", "Munjka Gam", "Trikon Baug", "Nyaragam Chokadi", "Vinodnagar", "Madhapar Gam", "-", "Saurashtra University", "Vinodnagar", "Jivraj Park", "Om Resi.", "Trikon Baug", "Saurashtra University", "Trikon Baug", "Saurashtra University", "-", "-", "-", "S.R.P. Camp", "-", "-", "Ghanteshvar S.R.P. Camp", "Ratanpar", "-", "Trikon Baug"]

    while True:
        try:
            bus_number = int(input("Input bus no.: "))
            SOURCE, DESTINATION, URL = get_bus_route(bus_number, sData, dData)
            if URL.startswith("Invalid"):
                print(URL)
                continue
            print(f"Source: {SOURCE}")
            print(f"Destination: {DESTINATION}")
            print(f"URL: {URL}")
        except ValueError:
            print("Invalid input. Please enter a valid bus number.")

if __name__ == "__main__":
    main()
sData=["-", "Saurashtra University", "Pradyuman Park", "Jivraj Park", "Aajidam ", "Raiya Gaam", "Santoshinagar", "Bajrangvadi Circle", "Greenland Chokadi", "Arpit Eng. College (Hadala Gam)", "-", "Shapar Veraval", "-", "Kothariya Chokadi", "Kothariya Gam", "G.I.D.C. Gate 3", "Kothariyagam", "Saurashtrar University", "Aajidam ", "131 Slam Quarter", "Ghanteshvar S.R.P. Camp", "Marketing Yard", "-", "Mavdi Gam", "G.I.D.C. Gate 3", "131 Slam Quarter", "Santoshinagar", "Raiyadhar Salam Quarter", "Gujarat Housing Quarter", "-", "Trikon Baug circular", "-", "Parsananagar", "Ashapura Mandir", "Marketing Yard", "Shapar Veraval", "Bhakatinagar Circle", "Chhatrapati Shivaji Township", "Aajidam ", "-", "Santoshinagar", "Gangotri Park", "Greenland Chokadi", "Akshar Vatika", "Tramba Gam", "Ratanpar", "Arpit Eng. College (Hadala Gam)", "Kothariyagam", "-", "-", "-", "Punit Nagar", "-", "-", "Kothariya Chokadi", "Gondal Chokadi", "-", "Government Eng. College"]
dData=["-", "Trikon Baug", "Raiya Gaam", "Madhapar Chokadi", "G.I.D.C. Gate 3", "Tramba", "Tramba Gam", "Bhakatinagar Circle", "Labhubhai Engineering College", "Saurashtra University", "-", "Trikon Baug", "-", "Lal bahadur shastriavas", "Navagam", "Kothariya Gam", "Saurashtra University", "Tramba Gam", "G.I.D.C. Gate 3", "Vavdi Gam", "Shapar Veraval", "Shantiniketan aveue (Raiya Gam)", "-", "Pradyuman Park", "Trikon Baug", "Jivraj Park", "Vavdi Gam", "Trikon Baug", "Jivraj Park", "-", "Trikon Baug", "-", "Tramba Gam", "Parsananagar", "Munjka Gam", "Trikon Baug", "Nyaragam Chokadi", "Vinodnagar", "Madhapar Gam", "-", "Saurashtra University", "Vinodnagar", "Jivraj Park", "Om Resi.", "Trikon Baug", "Saurashtra University", "Trikon Baug", "Saurashtra University", "-", "-", "-", "S.R.P. Camp", "-", "-", "Ghanteshvar S.R.P. Camp", "Ratanpar", "-", "Trikon Baug"]
  

while True:
    try:
        bus = int(input("Input bus no.: "))
        if bus < 0 or bus >= len(sData):
            print("Invalid bus number. Please try again.")
            continue
        SOURCE = "+".join(sData[bus].split())
        DESTINATION = "+".join(dData[bus].split())
        URL = f"https://www.google.com/maps/dir/{SOURCE}+bus+stop,+Rajkot,+Gujarat/${DESTINATION}+bus+stop,+Rajkot,+Gujarat/"
        print(f"Source: {SOURCE}")
        print(f"Destination: {DESTINATION}")
        print(f"URL: {URL}")
    except ValueError:
        print("Invalid input. Please enter a valid bus number.")