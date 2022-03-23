
from dataclasses import dataclass

@dataclass
class HourlyEmployee():

    name:str
    id :int
    comission:float = 100
    contract_landed:float = 0
    pay_rate:float = 0
    hours_worked:int = 0
    employer_cost:float = 1000

    def compute_pay(self) ->float:
        return (self.pay_rate * self.hours_worked
                + self.employer_cost
                +self.comission * self.contract_landed
                ) 
@dataclass
class SalariedEmployee():

    name:str
    id :int
    comission:float = 100
    contracts_landed:float = 0
    pay_rate:float = 0
    monthly_salary:float = 0
    percentage:float = 1

    def compute_pay(self) ->float:
        return (self.monthly_salary * self.percentage
                +self.comission * self.contracts_landed
                ) 
        
def main():
    """Main Function"""
    henry =HourlyEmployee(name="Henry" ,id=123456 ,pay_rate=50,hours_worked=100)
    print(
        f"{henry.name} worked for {henry.hours_worked} hours has earned ${henry.compute_pay()}"
    )

    sarah = SalariedEmployee(
        name="Sarah", id=47832, monthly_salary=5000, contracts_landed=10
    )
    print(
        f"{sarah.name} landed {sarah.contracts_landed} contracts and earned ${sarah.compute_pay()}."
    )

if __name__ == "__main__":
    main()

