const { Jumlah, Kurang, Kali, Bagi } = require('./Helper');

describe('Unit test untuk fungsi matematika', () => {
  test('penjumlahan 2 + 3 = 5', () => {
    expect(Jumlah(2, 3)).toBe(5);
  });

  test('pengurangan 5 - 2 = 3', () => {
    expect(Kurang(5 - 2)).toBe(3);
  });

  test('perkalian 2 * 4 = 8', () => {
    expect(Kali(2, 4)).toBe(8);
  });

  test('pembagian 6 / 2 = 3', () => {
    expect(Bagi(6, 2)).toBe(3);
  });
});
