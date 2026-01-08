const API_BASE_URL = process.env.REACT_APP_API_URL || "http://localhost:5000/api";

// Fetch portfolio data
export const fetchPortfolioData = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/portfolio`);
    if (!response.ok) {
      throw new Error("Failed to fetch portfolio data");
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching portfolio data:", error);
    throw error;
  }
};

// Fetch projects data
export const fetchProjectsData = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/projects`);
    if (!response.ok) {
      throw new Error("Failed to fetch projects data");
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching projects data:", error);
    throw error;
  }
};

// Fetch experience data
export const fetchExperienceData = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/experience`);
    if (!response.ok) {
      throw new Error("Failed to fetch experience data");
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching experience data:", error);
    throw error;
  }
};

// Fetch certifications data
export const fetchCertificationsData = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/certifications`);
    if (!response.ok) {
      throw new Error("Failed to fetch certifications data");
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching certifications data:", error);
    throw error;
  }
};

// Fetch testimonials data
export const fetchTestimonialsData = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/testimonials`);
    if (!response.ok) {
      throw new Error("Failed to fetch testimonials data");
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching testimonials data:", error);
    throw error;
  }
};

// Fetch articles data
export const fetchArticlesData = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/articles`);
    if (!response.ok) {
      throw new Error("Failed to fetch articles data");
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching articles data:", error);
    throw error;
  }
};

// Fetch services data
export const fetchServicesData = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/services`);
    if (!response.ok) {
      throw new Error("Failed to fetch services data");
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching services data:", error);
    throw error;
  }
};

// Submit contact form
export const submitContactForm = async (data) => {
  try {
    const response = await fetch(`${API_BASE_URL}/contact`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    if (!response.ok) {
      throw new Error("Failed to submit contact form");
    }
    return await response.json();
  } catch (error) {
    console.error("Error submitting contact form:", error);
    throw error;
  }
};

// Subscribe to newsletter
export const subscribeToNewsletter = async (email) => {
  try {
    const response = await fetch(`${API_BASE_URL}/newsletter`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email }),
    });
    if (!response.ok) {
      throw new Error("Failed to subscribe to newsletter");
    }
    return await response.json();
  } catch (error) {
    console.error("Error subscribing to newsletter:", error);
    throw error;
  }
};

// Get newsletter subscribers (admin only)
export const getNewsletterSubscribers = async (token) => {
  try {
    const response = await fetch(`${API_BASE_URL}/newsletter`, {
      headers: {
        "Authorization": `Bearer ${token}`,
      },
    });
    if (!response.ok) {
      throw new Error("Failed to fetch newsletter subscribers");
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching newsletter subscribers:", error);
    throw error;
  }
};

