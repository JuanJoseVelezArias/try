import cmd

class Calculator(cmd.Cmd):
    intro = "Calculadora simple. Ingresa 'help' para ver los comandos disponibles."
    prompt = "> "

    def do_add(self, args):
        'Suma dos números: add x y'
        x, y = map(float, args.split())
        print(x + y)

    def do_subtract(self, args):
        'Resta dos números: subtract x y'
        x, y = map(float, args.split())
        print(x - y)

    def do_multiply(self, args):
        'Multiplica dos números: multiply x y'
        x, y = map(float, args.split())
        print(x * y)

    def do_divide(self, args):
        'Divide dos números: divide x y'
        x, y = map(float, args.split())
        if y != 0:
            print(x / y)
        else:
            print("No es posible dividir por cero.")

    def do_exit(self, args):
        'Sale del intérprete: exit'
        print("¡Hasta luego!")
        return True

if __name__ == "__main__":
    Calculator().cmdloop()
