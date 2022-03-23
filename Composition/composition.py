
from typing import Optional
from dataclasses import dataclass
from abc import ABC, abstractmethod 

@dataclass
class Employee(ABC):
    name:str
    id : int

    @abstractmethod
    def compute_pay(self) -> float:
        """TO be implemented"""

        

@dataclass
class Commission(ABC):

    @abstractmethod
    def get_payment(self) -> float:
        """To be implemented"""

class Contract(ABC):
    """Represents a contract anda payment process for a particular employeee."""

    @abstractmethod
    def get_payment(self) -> float:
        """Compute how much to pay an employee under this contract."""


@dataclass
class HourlyEmplyee(Employee):

    name:str
    id :int
    comission:float = 100
    contract_landed:float = 0
    pay_rate:float = 0
    hours_worked:int = 0
    emplyer_cost:float = 1000

    def compute_pay(self) ->float:
        return (self.pay_rate * self.hours_worked
                + self.emplyer_cost
                +self.comission * self.contract_landed
                ) 

class SalariedEmployee():

    name:str
    id :int
    comission:float = 100
    contract_landed:float = 0
    pay_rate:float = 0
    hours_worked:int = 0
    emplyer_cost:float = 0

    def compute_pay(self) ->float:
        return (self.pay_rate * self.hours_worked
                + self.emplyer_cost
                +self.comission * self.contract_landed
                ) 
        
def main():
    """Main Function"""
    henry =HourlyEmplyee(name="Henry" ,id=123456 ,pay_rate=50,hours_worked=100)
    print(
        f"{henry.name} worked for {henry.hours_worked} hours has earned ${henry.compute_pay()}"
    )

if __name__ == "__main__":
    main()

