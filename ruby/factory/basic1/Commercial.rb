require_relative 'Plan.rb'
class Commercial < Plan
    def initialize
        @rate = 10
        @mode = 'Commercial'
    end 
end