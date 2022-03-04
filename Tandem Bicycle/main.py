# fastest == false
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if not fastest:
        reverseArrayinPlace(redShirtSpeeds)

    totalSpeed = 0
    for idx in range(len(redShirtSpeeds)):
        rider1 = redShirtSpeeds[idx]
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - idx -1]
        totalSpeed += max(rider1, rider2)
    return totalSpeed

def reverseArrayinPlace(array):
    start = 0
    end = len(array) -1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1


print(tandemBicycle([5,5,3,9,2], [3,6,7,2,1], False))

# if you create a paramater for if fastest == true
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if fastest:
        reverseArrayinPlace(redShirtSpeeds)

    totalSpeed = 0
    for idx in range(len(redShirtSpeeds)):
        rider1 = redShirtSpeeds[idx]
        rider2 = blueShirtSpeeds[idx]
        totalSpeed += max(rider1, rider2)
    return totalSpeed

def reverseArrayinPlace(array):
    start = 0
    end = len(array) -1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1