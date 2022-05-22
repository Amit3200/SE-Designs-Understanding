class Plan
    attr_accessor :rate
    attr_accessor :mode
    def initialize
        @rate = 5.5
        @mode = 'Default'
    end

    def calculate_amount(item, units)
        amount = units * rate
        return amount
    end

    def get_bill(item, units)
        amount = calculate_amount(item, units)
        msg = "#{item} [Bill -> #{@mode}] : #{amount}."
        print_bill(msg)
    end

    def print_bill(msg)
        puts msg 
    end
end