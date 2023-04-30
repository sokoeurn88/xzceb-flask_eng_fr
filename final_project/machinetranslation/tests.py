describe('frenchToEnglish', () => {
  it('returns null when input is null', async () => {
    const result = await frenchToEnglish(null);
    assert.strictEqual(result, null);
  });
});


describe('englishToFrench', () => {
  it('returns null when input is null', async () => {
    const result = await englishToFrench(null);
    assert.strictEqual(result, null);
  });
});

