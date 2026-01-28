package money;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Test;

public class MoneyTest {
    @Test
    public void testMultiplication() {
        var five = new Dollar(5);
        assertThat(five.times(2)).isEqualTo(new Dollar(10));
        assertThat(five.times(3)).isEqualTo(new Dollar(15));
    }

    @Test
    public void testEquality() {
        assertThat(new Dollar(5).equals(new Dollar(5))).isTrue();
        assertThat(new Dollar(5).equals(new Dollar(6))).isFalse();
    }
}
