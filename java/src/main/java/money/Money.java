package money;

class Money {
    protected int amount;

    @Override
    public boolean equals(Object object) {
        var money = (Money) object;
        return amount == money.amount;
    }
}
