import boto3
client = boto3.client('rekognition')
with open("input.jpg", "rb") as image:
    image_bytes = image.read()

    # detect labels (objects / scene)
    response = client.detect_labels(Image={'Bytes': image_bytes})
    print("Detected labels:")
    for label in response['Labels']:
        print(f" - {label['Name']} : {label['Confidence']:.2f}%")
    