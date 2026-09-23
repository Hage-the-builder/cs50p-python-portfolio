import sys
import requests # type: ignore

def main():

    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
                                                    # make sure that there is a input after typing "python bitcoin.py"

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
                                                                #makes sure that the said input is a number

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=64916844ce22c8317bc4e97f5ff08e543b2882f7cce6e4cf7f2d773e818597f7")  #my personal API code :)

        data = response.json()
                                            # Request the current bitcoin from the CoinDesk API

        rate = float(data["data"]["priceUsd"])
                                                        # looks through the data to find the price

    except (requests.RequestException, KeyError, ValueError, IndexError):
        sys.exit("Failed to fetch current Bitcoin price data")
                                                                            #message upon failer HAS TO BE THERE TO COMPLETE THE CODE

    cost = bitcoins * rate
    print(f"${cost:,.4f}")
                                    # Calculate the bitcoin total cost with commas and to 4 decimal points
if __name__ == "__main__":
    main()
                        # has to be threr for the main definition function
