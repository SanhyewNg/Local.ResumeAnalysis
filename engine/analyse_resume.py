import json
from .utils import extract_text_from_file, get_gemini_response

resume_extract_prompt = """
Objective:  Parse a text-formatted resume efficiently and extract diverse applicant's data into a structured JSON format that adheres to the provided TypeScript interface schema.

Input: Text-formatted applicant's resume.

Steps:
1. Analyze Structure: Examine the text-formatted resume to understand its organization and identify key sections (e.g., education, experience, skills).
2. Convert to JSON: Map the extracted information to the corresponding fields in the schema, creating a structured JSON representation.
3. Optimize Output: Ensure the JSON is well-formatted, error-free, and handles missing values appropriately.
4. Handle Variations: Account for different resume styles and formatting to accurately extract relevant data.

Consider following TypeScript Interface for JSON schema:
```

interface Education {
  degree_and_program: string;
  university: string;
  location: string;
  date_of_completion: string;
  grade: string;
  coursework?: string;
}

interface Skill {
  name: string;
  skills: string;
}

interface Work {
  role: string;
  company: string;
  location: string;
  from: string;
  to: string;
  description: string[];
}

interface Project {
  name: string;
  description: string[];
}

interface RESUME_DATA_SCHEMA {
  name: string;
  email: string;
  phone: string;
  website: string;
  location: string;
  education: Education[];
  skills: Skill[];
  work_experience: Work[];
  projects: Project[];
}
```

Desired Output: Write the Well-formatted JSON adhering to the RESUME_DATA_SCHEMA schema, handling missing values with empty strings or "None".
<JSON_OUTPUT_ACCORDING_TO_RESUME_DATA_SCHEMA>

I want to convert the output directly to JSON hence, the results should contain valid JSON only, without any delimiter or characters making invalid JSON format.
"""

def analyse_resume(resume):
    resume_text = extract_text_from_file(resume)
    
    gemini_response = get_gemini_response(resume_extract_prompt + "--" + resume_text)
    # logger.debug(f"resume_to_json response: {res}")

    try:
        response = gemini_response.replace("```json", "").replace("```JSON", "").replace("```", "").replace("None","").replace("JSON\n", "")
        resume_analysis_result = json.loads(response)
        # logger.debug(f"resume_to_json data: {resume_analysis_result}")
        return resume_analysis_result

    except Exception as e:
        # logger.error(f"Error: error converting resume to json.\nres:{res}\nDetailed error: {e}")
        return f"Error: error converting resume to json"
            
        
