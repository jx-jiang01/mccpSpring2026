# HKBU GenAI Platform API Documentation

## Source
[Embeddings Swagger Documentation](https://genai.hkbu.edu.hk/general/specification/embeddings-swagger?fullscreen=true)

## API Endpoint

**Base URL**: `https://genai.hkbu.edu.hk/api/v0/rest`

**Note**: The endpoint is **NOT** `https://hkbu-genai.openai.azure.com/` but rather `https://genai.hkbu.edu.hk/api/v0/rest`

## Embeddings API

### Endpoints

1. **Standard Endpoint:**
   ```
   POST /deployment/{modelDeploymentName}/embedding
   ```

2. **OpenAI-Compatible Endpoint:**
   ```
   POST /openai/deployment/{modelDeploymentName}/embedding
   ```
   
   **Recommended**: Use this endpoint for OpenAI-compatible SDKs (like LangChain)

### Available Models

| Model Name | API Version |
|------------|-------------|
| text-embedding-3-large | 2023-12-01-preview |
| text-embedding-3-small | 2023-12-01-preview |

**Note**: Models may also support other API versions (see API Version section)

### API Versions

Available API versions:
- `2023-12-01-preview` (Default)
- `2024-02-15-preview`
- `2024-02-01`
- `2024-05-01-preview`

**Default**: `2023-12-01-preview`

### Parameters

**Path Parameter:**
- `modelDeploymentName` (string, required): The deployment name of the embedding model
  - Options: `text-embedding-3-large`, `text-embedding-3-small`

**Query Parameter:**
- `api-version` (string, required): The API version to use for this operation
  - Default: `2023-12-01-preview`
  - Options: `2023-12-01-preview`, `2024-02-15-preview`, `2024-02-01`, `2024-05-01-preview`

**Request Body:**
- Content-Type: `application/json`
- Schema: `CreateEmbeddingDto` (see Swagger documentation for details)

### Authentication

API key authentication is required (Authorization header)

### Example Usage

**Endpoint URL:**
```
POST https://genai.hkbu.edu.hk/api/v0/rest/openai/deployments/text-embedding-3-small/embeddings?api-version=2023-12-01-preview
```

**Headers:**
```
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

**Request Body:**
```json
{
  "input": "Your text to embed"
}
```

## Configuration for LangChain

Since the HKBU API uses a custom endpoint structure (not standard Azure OpenAI), you'll need to:

1. Use the OpenAI-compatible endpoint: `/openai/deployment/{modelDeploymentName}/embedding`
2. Set base URL to: `https://genai.hkbu.edu.hk/api/v0/rest`
3. Include `api-version` as a query parameter
4. Use the API key in Authorization header

**Note**: Standard LangChain Azure OpenAI integrations may not work directly due to the custom endpoint structure. You may need to create a custom embedding class or use the OpenAI SDK directly with custom base URL.

## Testing

The documentation provides links to:
- Postman for Windows
- Command line – Curl
- Python Example

Refer to the [Swagger documentation](https://genai.hkbu.edu.hk/general/specification/embeddings-swagger?fullscreen=true) for detailed examples.
