# AlgoDM-Fall2023-Team9-Assignment-5


### PART 1: Fashion Image Annotation with OpenAI GPT4 Vision API and Snowflake Database

#### Introduction
This section focuses on fashion image annotation using the OpenAI GPT4 Vision to text API and storing the annotations in a Snowflake database.

#### Fashion Image Annotation
1. **Tags/Annotations:**
   - Review popular fashion retailer navigation bars (e.g., Macy's, Amazon) for inspiration.
   - Proposed Tags:
     1. Clothing Type
     2. Color
     3. Brand
     4. Pattern
     5. Occasion
     6. Season
     7. Material
     8. Size
     9. Price Range
     10. Style

2. **JSON Template:**
   - Create a JSON template for annotations:
     ```json
     {
       "image_path": "/path/to/image.jpg",
       "annotations": ["clothing", "blue", "Nike", "striped", "casual", "spring", "cotton", "medium", "$50-$100", "sports"]
     }
     ```

3. **OpenAI GPT4 Vision API Script:**
   - Develop a Python script that:
     - Iterates through images in an Amazon S3 bucket.
     - Generates annotations for each image using the GPT4 Vision API.
     - Performs a bulk upsert into a Snowflake database.

4. **Snowflake Database:**
   - Set up a Snowflake database to store image annotations.
   - Define a schema that accommodates the proposed tags.
   - Ensure proper indexing for efficient retrieval.

#### Usage
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up environment variables for API keys and Snowflake connection.
4. Run the annotation script as per the provided instructions.

### PART 2: Multi-Modal Retrieval Model

#### Introduction
This section focuses on building a multi-modal retrieval model that can find similar images and text tags given an image or text input.

#### Multi-Modal Retrieval Model
1. **Image Similarity:**
   - Utilize LlamaIndex and CLIP embeddings for:
     - Encoding query text for text index using ADA.
     - Encoding query text for the image index using CLIP.
   - Implement a script that performs multi-modal retrieval based on image captions.

2. **Text-Based Retrieval:**
   - Implement a script that retrieves images based on a given text query.

#### Usage
1. Ensure that the Snowflake database is populated with annotated images.
2. Run the multi-modal retrieval script as per the provided instructions.
3. Review the retrieved images and associated text tags.

### PART 3: Streamlit App Interface for Multi-Modal Retrieval

#### Introduction
This section focuses on creating a user-friendly Streamlit app interface for the multi-modal retrieval model developed in Part 2.

#### Streamlit App
1. **User Interface:**
   - Develop a Streamlit app with an intuitive interface.
   - Include options for both image and text-based queries.
   - Display retrieved images and associated text tags.

2. **Integration with Multi-Modal Retrieval:**
   - Integrate the Streamlit app with the multi-modal retrieval model.
   - Allow users to input queries and receive relevant images and text tags.

#### Usage
1. Run the Streamlit app using `streamlit run app.py`.
2. Open the app in a web browser.
3. Input queries and explore the multi-modal retrieval capabilities.

Codelab Document: https://codelabs-preview.appspot.com/?file_id=1mV2LItx7RyLIjZJU_M3X0r2rfCNGqYndMvRGMJa8K4c#0
