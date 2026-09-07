from abc import ABC, abstractmethod

# ============================================================================
# 1. ABSTRACTION & ENCAPSULATION
# ============================================================================
class Vehicle(ABC):
    def __init__(self, v_id: str, brand: str, model: str, price_per_day: float):
        self.v_id = v_id
        self.brand = brand
        self.model = model
        
        # Private attributes (Encapsulation)
        self.__price_per_day = price_per_day
        self.__is_available = True

    # Getter & Setter for encapsulation
    def get_price(self) -> float:
        return self.__price_per_day

    def is_available(self) -> bool:
        return self.__is_available

    def set_available(self, status: bool):
        self.__is_available = status

    # Abstract Method (Abstraction)
    @abstractmethod
    def calculate_price(self, days: int) -> float:
        pass


# ============================================================================
# 2. INHERITANCE & POLYMORPHISM
# ============================================================================
class Car(Vehicle):
    def calculate_price(self, days: int) -> float:
        # Car includes a flat ₹500/day insurance fee
        return (self.get_price() + 500) * days


class Bike(Vehicle):
    def calculate_price(self, days: int) -> float:
        # Bike gets a 10% eco-discount
        return (self.get_price() * 0.90) * days


class Truck(Vehicle):
    def calculate_price(self, days: int) -> float:
        # Truck includes a ₹1500 heavy vehicle surcharge
        return (self.get_price() + 1500) * days


# ============================================================================
# 3. FLEET MANAGER WITH INTERACTIVE USER INPUT
# ============================================================================
class RentalSystem:
    def __init__(self):
        # Pre-loading some initial vehicles (Prices in INR ₹)
        self.fleet = [
            Car("C1", "Toyota", "Camry", 3000.0),
            Bike("B1", "Yamaha", "R15", 800.0),
            Truck("T1", "Volvo", "FH16", 8000.0)
        ]

    def show_vehicles(self):
        print("\n--- AVAILABLE VEHICLES ---")
        available = [v for v in self.fleet if v.is_available()]
        if not available:
            print("No vehicles available right now!")
            return
        
        for v in available:
            print(f"ID: {v.v_id} | Type: {type(v).__name__} | {v.brand} {v.model} | Rate: ₹{v.get_price():.2f}/day")

    def rent_vehicle(self):
        self.show_vehicles()
        v_id = input("\nEnter Vehicle ID to rent: ").strip().upper()
        
        # Find vehicle
        vehicle = next((v for v in self.fleet if v.v_id == v_id and v.is_available()), None)
        if not vehicle:
            print("Invalid ID or vehicle not available.")
            return

        name = input("Enter your name: ").strip()
        try:
            days = int(input("Enter number of rental days: "))
            if days <= 0:
                print("Days must be greater than 0.")
                return
        except ValueError:
            print("Invalid input! Days must be a number.")
            return

        # Polymorphic price calculation
        total = vehicle.calculate_price(days)
        vehicle.set_available(False)

        print("\n" + "="*35)
        print("         RENTAL RECEIPT         ")
        print("="*35)
        print(f"Customer Name : {name}")
        print(f"Vehicle       : {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        print(f"Duration      : {days} days")
        print(f"Total Cost    : ₹{total:.2f}")
        print("="*35)

    def return_vehicle(self):
        v_id = input("\nEnter Vehicle ID to return: ").strip().upper()
        vehicle = next((v for v in self.fleet if v.v_id == v_id and not v.is_available()), None)
        
        if vehicle:
            vehicle.set_available(True)
            print(f"Vehicle {vehicle.v_id} successfully returned!")
        else:
            print("Invalid ID or this vehicle was not rented.")


# ============================================================================
# 4. MAIN MENU
# ============================================================================
def main():
    system = RentalSystem()
    
    while True:
        print("\n===== VEHICLE RENTAL SYSTEM =====")
        print("1. View Available Vehicles")
        print("2. Rent a Vehicle")
        print("3. Return a Vehicle")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            system.show_vehicles()
        elif choice == "2":
            system.rent_vehicle()
        elif choice == "3":
            system.return_vehicle()
        elif choice == "4":
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid selection! Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()