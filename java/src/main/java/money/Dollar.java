package money;

class Dollar {
    private int amount;

    Dollar(int amount) {
        this.amount = amount;
    }

    Dollar times(int multiplier) {
        return new Dollar(amount * multiplier);
    }

    @Override
    public boolean equals(Object object) {
        var dollar = (Dollar) object;
        return amount == dollar.amount;
    }
}
