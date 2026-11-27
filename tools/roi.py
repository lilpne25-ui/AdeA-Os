"""Modelo hipotético de ROI. Biblioteca estándar; no usa datos reales."""
import argparse
from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Plan:
    name: str
    initial: float
    monthly: float
    months: int
    users: int
    hours: float
    adoption: float
    realization: float
    rate: float = 300

    def calculate(self):
        if not (0 <= self.months <= 12 and 0 <= self.adoption <= 1 and 0 <= self.realization <= 1):
            raise ValueError("Invalid months, adoption or realization")
        if min(self.initial, self.monthly, self.users, self.hours, self.rate) < 0:
            raise ValueError("Negative input")
        hours = self.users * self.hours * 4.33 * self.adoption
        monthly_benefit = hours * self.rate * self.realization
        cost = self.initial + 12 * self.monthly
        benefit = monthly_benefit * (12 - self.months)
        net = benefit - cost
        payback = (self.months + (self.initial + self.months * self.monthly) /
                   (monthly_benefit - self.monthly)) if monthly_benefit > self.monthly else None
        return dict(hours=hours, monthly_benefit=monthly_benefit, cost=cost,
                    benefit=benefit, net=net, roi=net/cost*100 if cost else None,
                    payback=payback)

PLANS = (
    Plan("A", 80000, 6000, 2, 10, 4, .75, .60),
    Plan("B", 200000, 12000, 4, 20, 5, .75, .65),
    Plan("C", 500000, 25000, 7, 40, 6, .80, .70),
)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--realization-factor", type=float, default=1)
    parser.add_argument("--rate", type=float, default=300)
    args = parser.parse_args()
    if not 0 <= args.realization_factor <= 1 or args.rate < 0:
        parser.error("factor must be 0..1; rate must be nonnegative")
    for p in PLANS:
        p = replace(p, realization=p.realization * args.realization_factor, rate=args.rate)
        m = p.calculate()
        print(p.name, {k: round(v, 2) if v is not None else None for k, v in m.items()})

if __name__ == "__main__":
    main()
