#Jakub Grzebielucha 59599 -- projekt zaliczeniowy semestru Python 2 -- Generator liczb pierwszych
#moduł main -- funkcja uruchamiająca generator poprzez funkcje main()
#moduł generator -- zawiera 2 funkcje składane, które są odpowiedzialne za poprawne działanie generatora
#moduł utils -- zawiera funkcje, która odpowiada za zapisanie liczb wygenerowanych do osobnego pliku tekstowego
#moduł test-unittest -- zawiera klasę, która odpowiada za sprawdzenie poprawnosci działania generatora.
#result.txt -- jest to plik tekstowy, który zapisuje liczby pierwsze wygenerowane przez generator

from generator import prime_generator
from utils import save_to_file

def main():
    try:
        start = int(input("Enter the beginning of the range: "))
        end = int(input("Enter the end of the range: "))

        if start > end:
            raise ValueError("The beginning cannot be greater than the end.")

        primes = list(prime_generator(start, end))
        print("Prime numbers in indicated range:", primes)
        save_to_file(primes, "result.txt")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
