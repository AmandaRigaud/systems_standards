from abc import ABC, abstractmethod

#  Strategy Pattern
# O padrão Strategy define estratégias que podem ser intercambiáveis.
class SalePricingStrategy(ABC):
    @abstractmethod
    def get_total(self, sale):
        pass


class PercentDiscountStrategy(SalePricingStrategy):
    def __init__(self, percentage):
        self.percentage = percentage
    
    def get_total(self, sale):
        return sale.total * (1 - self.percentage / 100)

class AbsoluteDiscountStrategy(SalePricingStrategy):
    def __init__(self, discount, threshold):
        self.discount = discount
        self.threshold = threshold
    
    def get_total(self, sale):
        if sale.total < self.threshold:
            return sale.total
        return sale.total - self.discount
        

# Sale class
class Sale:
    def __init__(self, total):
        self.total = total

# Singleton Factory Pattern
# O padrão Singleton garante que uma classe tenha apenas uma instância e forneça um ponto de acesso global a essa instância.
# O padrão Factory é usado para criar objetos sem expor a lógica de criação ao cliente, permitindo que a fábrica decida qual tipo de objeto retornar.
class PricingStrategyFactory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PricingStrategyFactory, cls).__new__(cls)
        return cls._instance

    def get_pricing_strategy(self, strategy_type):
        if strategy_type == "percent":
            return PercentDiscountStrategy(10)  # Exemplo: 10% de desconto
        elif strategy_type == "absolute":
            return AbsoluteDiscountStrategy(10, 200)  # Exemplo: R$10 de desconto para vendas acima de R$200

#  Adapter Pattern
# O padrão Adapter tem como função permitir que classes com interfaces incompatíveis possam trabalhar juntas, sem que seja necessário alterar o código dessas classes.
class SaleAdapter:
    def __init__(self, sale):
        self.sale = sale

    def adapt_sale(self):
        # Adapta o objeto sale de alguma forma para outra interface
        return self.sale

# Exemple
if __name__ == "__main__":
    sale = Sale(300)
    factory = PricingStrategyFactory()
    strategy = factory.get_pricing_strategy("percent")
    adapted_sale = SaleAdapter(sale).adapt_sale()
    print(f"Total com desconto: {strategy.get_total(adapted_sale)}")
