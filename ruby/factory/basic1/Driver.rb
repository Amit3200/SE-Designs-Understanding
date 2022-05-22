require_relative 'PlanFactory.rb'
class Driver
    def initialize
    end

    def scenario_1
        plan_factory_client = PlanFactory.new('Regular').get_client
        plan_factory_client.get_bill('Bags',15)
    end

    def scenario_2
        plan_factory_client = PlanFactory.new('Commercial').get_client
        plan_factory_client.get_bill('Bags',15)
    end

    def scenario_3
        plan_factory_client = PlanFactory.new.get_client
        plan_factory_client.get_bill('Bags',15)
    end
end

main = Driver.new 
main.scenario_1
main.scenario_2
main.scenario_3