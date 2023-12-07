const fiveOfAKind = hand => Object.keys(hand).length === 1;
const fourOfAKind = hand => Object.keys(hand).length === 2 && Math.max(...Object.values(hand)) === 4;
const fullHouse = hand => Object.keys(hand).length === 2 && Math.max(...Object.values(hand)) === 3;
const threeOfAKind = hand => Object.keys(hand).length === 3 && Math.max(...Object.values(hand)) === 3;
const twoPair = hand => Object.keys(hand).length === 3 && Math.max(...Object.values(hand)) === 2;
const onePair = hand => Object.keys(hand).length === 4 && Math.max(...Object.values(hand)) === 2;
const highCard = hand => true;

const alphaCardScores = {
  T: 10,
  J: 1,
  Q: 12,
  K: 13,
  A: 14
}

const getCardScore = c => alphaCardScores[c] || Number(c)

const handTypes = [
  fiveOfAKind,
  fourOfAKind,
  fullHouse,
  threeOfAKind,
  twoPair,
  onePair,
  highCard,
]

/**
 *
 * @param {string} input
 */
module.exports = (input) => {
  let hands = input.split("\n").filter(Boolean).map(s => {
    const [hand, bid] = s.split(" ");
    let jokers = 0
    const parsedHand = Array.from(hand).reduce((acc, card) => {
      if (card === "J") {
        jokers++
      } else {
        acc[card] = (acc[card] || 0) + 1
      }
      return acc;
    }, {})
    const largestCountCardType = Object.keys(parsedHand).sort((a, b) => parsedHand[b] - parsedHand[a])[0]
    parsedHand[largestCountCardType] += jokers;
    const handScore = handTypes.length - handTypes.findIndex(ht => ht(parsedHand))
    return { score: handScore, hand: Array.from(hand), bid}
  })
  hands = hands.sort((a, b) => {
    if(a.score !== b.score) {
      return a.score - b.score
    }
    for(let i = 0; i < a.hand.length; i++) {
      if(a.hand[i] !== b.hand[i]) {
        return getCardScore(a.hand[i]) - getCardScore(b.hand[i]);
      }
    }
    return 0;
  })
  return hands.map(({ bid }, index) => (index + 1) * Number(bid))
    .reduce((a, b) => a + b)
}
