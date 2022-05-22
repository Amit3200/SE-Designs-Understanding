require_relative 'Plan.rb'
require_relative 'Commercial.rb'
require_relative 'Regular.rb'

class PlanFactory
    def initialize(plan = 'default')
        @plan = plan.downcase
    end

    def get_client
        case @plan
        when 'commercial'
            return Commercial.new
        when 'regular'
            return Regular.new
        else
            return Plan.new
        end
    end
end


